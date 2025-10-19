```json
{
  "id": "488cfe496741b246",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292202,
  "host_pid": "9e6742732c60:1",
  "hash": "37f318680d45899ff44262276b99f0178f01a7f123774211d0b51d848e5ccfe0",
  "cid": "QmV137f318680d45899ff44262276b99f0178f01a7f1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292202,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760292202
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "84b9f434465761edb26a3afb3d83625ef76280b75390289ad5bd1c849fd3dcf1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246289995
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 20104704, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285764, 'matching_hash': '1ab4d10c626d0dd7'}}}
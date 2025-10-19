```json
{
  "id": "955673270098ee07",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292427,
  "host_pid": "9e6742732c60:1",
  "hash": "be80db4bef836f46c1a03d2c333ddfbf9dd2c679f868a4d389d8edec843445b2",
  "cid": "QmV1be80db4bef836f46c1a03d2c333ddfbf9dd2c679",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292427,
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
      "evaluated_at": 1760292427
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
  "sig": "bcaf2e4854e7086b745a40e18f5dc9bd1a53e1ce3b5f2031b8c3cec64ee7d2cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244410720
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 13889485, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285763, 'matching_hash': 'eab520de73a5b8cf'}}}
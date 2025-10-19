```json
{
  "id": "bc82d15c42d34a66",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286812,
  "host_pid": "9e6742732c60:1",
  "hash": "0a7fa74eb357a53fa2b3cb8e4cf1be5a19dbabeec258d248d473337e96c7c0e9",
  "cid": "QmV10a7fa74eb357a53fa2b3cb8e4cf1be5a19dbabee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286812,
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
      "evaluated_at": 1760286812
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "abcf46406c5ff76dfa523134cb652fb0598c1796618981097c6c3d005b09224f"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000025069817
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 18059462, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285763, 'matching_hash': '107b8433ca6199ca'}}}
```json
{
  "id": "e67eb2ab90faf3cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293885,
  "host_pid": "9e6742732c60:1",
  "hash": "933cef2041523f31b6a6e4da4c3dc9a9e6b704844a33d2b8c2a228de86ab2757",
  "cid": "QmV1933cef2041523f31b6a6e4da4c3dc9a9e6b70484",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293885,
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
      "evaluated_at": 1760293885
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
  "sig": "c2c9e785482b3d59fe99b8fff4ea8ce93d196c24cfb42b9bdffe0db5d36c111a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032369849
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 94767052, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285764, 'matching_hash': '11b86d7f8733bf3d'}}}
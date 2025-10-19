```json
{
  "id": "cf3a95cd9770ec71",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292111,
  "host_pid": "9e6742732c60:1",
  "hash": "ed04e218e8510e41daac03bcca602fd51c285c0f82ca1650b1831035566e857a",
  "cid": "QmV1ed04e218e8510e41daac03bcca602fd51c285c0f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292111,
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
      "evaluated_at": 1760292111
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
  "sig": "0f2746a546a0e7892e0d871ecafab658808cb2c5b15a24a5f8c8716ea108c329"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021011137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 63293750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285764, 'matching_hash': '3868aeea45d72d6f'}}}
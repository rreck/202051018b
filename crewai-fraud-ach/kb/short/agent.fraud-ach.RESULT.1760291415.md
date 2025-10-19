```json
{
  "id": "210e0b99c2cff416",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291415,
  "host_pid": "9e6742732c60:1",
  "hash": "273ffac474c0fb24d29ac0bc35d9312ed4376d97e92e1f65cf047d86a73a5d4f",
  "cid": "QmV1273ffac474c0fb24d29ac0bc35d9312ed4376d97",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291415,
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
      "evaluated_at": 1760291415
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
  "sig": "c1ce9f9dbfb8fd9ef753a961f6df78e08ba54de2fc4259c1c7adf76248503a81"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248914863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285765, 'matching_hash': '9c0338b7ffb65590'}}}
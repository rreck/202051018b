```json
{
  "id": "60fd089f739b0900",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292669,
  "host_pid": "9e6742732c60:1",
  "hash": "4511202240fe3c0993bbc6edf5edb3c4394914efef91310d3ab90647d32577a8",
  "cid": "QmV14511202240fe3c0993bbc6edf5edb3c4394914ef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292669,
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
      "evaluated_at": 1760292669
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
  "sig": "2bd178fb4536313bccc3d132372810d86ba46b57f9e5c897882576dfafa72587"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021933242
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 51360722, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285765, 'matching_hash': '22fbbd19d3df08b1'}}}
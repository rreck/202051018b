```json
{
  "id": "96b8927e9ce68597",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288569,
  "host_pid": "9e6742732c60:1",
  "hash": "3f3adb4e72588bf8be206f9b8731a48eadaeb8a792862f39b748106352661ef8",
  "cid": "QmV13f3adb4e72588bf8be206f9b8731a48eadaeb8a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288569,
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
      "evaluated_at": 1760288569
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
  "sig": "95f8f903ea57785b6e08090106d3ab85f0dc43e5d3076cda87ef583e93bd748b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248025724
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 10997666, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285764, 'matching_hash': 'cc12810353983743'}}}
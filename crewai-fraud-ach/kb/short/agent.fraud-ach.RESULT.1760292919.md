```json
{
  "id": "707d48fd6250866e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292919,
  "host_pid": "9e6742732c60:1",
  "hash": "4e680565f86bcbe9af950a10ef2590f035285a32c0d28a474ef0d18514a395c6",
  "cid": "QmV14e680565f86bcbe9af950a10ef2590f035285a32",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292919,
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
      "evaluated_at": 1760292919
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
  "sig": "ec17de4c160fafd6b67a6760319d2867758ba4f1dc6ff553d0ea13838bd26a8a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156237747
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 16198208, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285763, 'matching_hash': 'b60e159429465bd2'}}}
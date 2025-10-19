```json
{
  "id": "6955c46c01837e81",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290472,
  "host_pid": "9e6742732c60:1",
  "hash": "1260936044a1e984b508eb6463ae5a2117115b52a6cb090fd031f932849a97af",
  "cid": "QmV11260936044a1e984b508eb6463ae5a2117115b52",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290472,
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
      "evaluated_at": 1760290472
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
  "sig": "b5c72647ba8a9e9dfb6afe2fe4b49871995e51fc492b9e5051c4be8c1145856f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023458666
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 92628031, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760284979, 'matching_hash': 'a7fb9dc83800d725'}}}
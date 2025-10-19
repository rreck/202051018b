```json
{
  "id": "480bb4bf24e39f35",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293405,
  "host_pid": "9e6742732c60:1",
  "hash": "659557551aed5b6ecfe24ea4a31bdd7d6d09752072ae47a57d73e2463140486e",
  "cid": "QmV1659557551aed5b6ecfe24ea4a31bdd7d6d097520",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293405,
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
      "evaluated_at": 1760293405
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
  "sig": "a9093b28dec64fe1b065d19b1ee98a829cf8653c21b867b6283bce6e90d5f84e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033242654
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 69487500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': '1355ad48790eb31b'}}}
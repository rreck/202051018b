```json
{
  "id": "ef41ba7b95f4c40c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292161,
  "host_pid": "9e6742732c60:1",
  "hash": "dc836e32e042a5bd557ea7380c5b784f08e3f809dd6cd082915941f63526ad04",
  "cid": "QmV1dc836e32e042a5bd557ea7380c5b784f08e3f809",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292161,
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
      "evaluated_at": 1760292161
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
  "sig": "cbc872f534072326704be797820234c634b88e717a0c95a5c030fbdee91504bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460708628
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285765, 'matching_hash': 'f97c6efa7b54b0cd'}}}
```json
{
  "id": "b99446bcde3b13e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294459,
  "host_pid": "9e6742732c60:1",
  "hash": "adb049ceae8d3e41cb071e2a6a379e598a87186edc0d8b4919fe5fdcac33a6bb",
  "cid": "QmV1adb049ceae8d3e41cb071e2a6a379e598a87186e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294459,
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
      "evaluated_at": 1760294459
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
  "sig": "1ad40d75de206c2c2084878e2c03eec7fd29da74911d416ccd72eeda1a2f53f5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596468860
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 17999940, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': 'e06c0748f018586e'}}}
```json
{
  "id": "8346e12a3b17b953",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290754,
  "host_pid": "9e6742732c60:1",
  "hash": "66cb2a524715fbee2db652f003b28fd8785b8bee1cf98e55ba37c288ae36a051",
  "cid": "QmV166cb2a524715fbee2db652f003b28fd8785b8bee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290754,
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
      "evaluated_at": 1760290754
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
  "sig": "8fbd5df8619f1dd9f05db0219025b8db0f2daae34ba2aef3f86a8bb47f47e7c4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026908362
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285765, 'matching_hash': '7a1f70b5e24e62dd'}}}
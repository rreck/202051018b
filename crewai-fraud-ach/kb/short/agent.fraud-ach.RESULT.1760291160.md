```json
{
  "id": "c461dd61fd13885b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291160,
  "host_pid": "9e6742732c60:1",
  "hash": "6121cd8c718a3936e400e6ff10624fc8021e17d7f179f417b4b61fd9740cc37b",
  "cid": "QmV16121cd8c718a3936e400e6ff10624fc8021e17d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291160,
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
      "evaluated_at": 1760291160
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
  "sig": "b401ba955d6fff7cee2af7a0ba71cefd1894be09b071724e1bdbbcdc9903fa0a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151422831
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 17174808, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285764, 'matching_hash': 'e9fc645b92693d6a'}}}
```json
{
  "id": "e1d178e01a379d7b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289588,
  "host_pid": "9e6742732c60:1",
  "hash": "3ea37b820c3064866776e63435c8fcbdc788fd50ddada2c4704efe0f39799cab",
  "cid": "QmV13ea37b820c3064866776e63435c8fcbdc788fd50",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289588,
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
      "evaluated_at": 1760289588
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
  "sig": "86536c290046434c9ea46f77a3465d2cebb423980fc2eb0e8d6e29194c315e08"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152240558
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 52953539, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285765, 'matching_hash': '0371944fd59dbf43'}}}
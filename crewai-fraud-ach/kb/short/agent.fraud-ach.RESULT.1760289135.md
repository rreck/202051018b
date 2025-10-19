```json
{
  "id": "fb11f85a5b08e211",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289135,
  "host_pid": "9e6742732c60:1",
  "hash": "4d386d1ccfb282c6ea7c02fa4ae39bc688d539a3812067e5e612a0fdedb5a6c4",
  "cid": "QmV14d386d1ccfb282c6ea7c02fa4ae39bc688d539a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289135,
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
      "evaluated_at": 1760289135
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
  "sig": "eeb9bcf3649cfe1743085c4c891547798af11d3a6ab8e4dacbe73f2569b2a02b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038480332
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285765, 'matching_hash': '8289eea4583ef54f'}}}
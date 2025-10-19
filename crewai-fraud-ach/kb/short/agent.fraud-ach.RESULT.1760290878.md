```json
{
  "id": "a01e4e79b4c96fb2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290878,
  "host_pid": "9e6742732c60:1",
  "hash": "4b7f8bade137b4a0e1ceec8f3bc504d7e322825c35afa738689987e89b2b352a",
  "cid": "QmV14b7f8bade137b4a0e1ceec8f3bc504d7e322825c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290878,
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
      "evaluated_at": 1760290878
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
  "sig": "5fa5da70971654484d84ffbdd86c19c9bdc37c68cb05f9bfe077ba03193ed326"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249334487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 33794544, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285765, 'matching_hash': 'f464ac6512a738da'}}}
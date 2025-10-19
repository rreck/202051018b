```json
{
  "id": "a510f02739d8afb4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287987,
  "host_pid": "9e6742732c60:1",
  "hash": "c37c060181f2ed1ce897ec7038b729204114b85dcef69333ec32325af5174995",
  "cid": "QmV1c37c060181f2ed1ce897ec7038b729204114b85d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287987,
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
      "evaluated_at": 1760287987
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
  "sig": "1863a3e8e04b732393a91543f1b2fdef12a1dea927eb0ed046ec1309ffffdcdb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460204606
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 10548633, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285763, 'matching_hash': 'ff63dbf095b2d177'}}}
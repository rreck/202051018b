```json
{
  "id": "a28e552a01ab3aca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290891,
  "host_pid": "9e6742732c60:1",
  "hash": "b0526c03793d649c0f75f1559f521d22257a91c2521c2521fba680f3b9640ee0",
  "cid": "QmV1b0526c03793d649c0f75f1559f521d22257a91c2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290891,
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
      "evaluated_at": 1760290891
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
  "sig": "87d82eac2f26ed4df49b00ee7277a5d220b5ecafada9e71ef85ff4e5b5678a7c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249862639
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 55722330, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285763, 'matching_hash': '8cd9f1a7b8ce269f'}}}
```json
{
  "id": "54a67e241ae6600a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294760,
  "host_pid": "9e6742732c60:1",
  "hash": "b052bb74b4922cb7fe74c8ae637fd48df5d3004956c39aabf7de516c1bbaceef",
  "cid": "QmV1b052bb74b4922cb7fe74c8ae637fd48df5d30049",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294760,
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
      "evaluated_at": 1760294760
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
  "sig": "0d461af15df066ef351218c19c615dffaaf1925fb5f92b5523748823c55d4665"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025853793
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 66346528, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': 'ff3a3f7dec7a702a'}}}
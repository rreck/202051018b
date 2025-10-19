```json
{
  "id": "df5b8881995223fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289257,
  "host_pid": "9e6742732c60:1",
  "hash": "b8fa914f2e081875baeb92bf7ddd9ad5692ec2ae94a27566230f9ae08c233cdb",
  "cid": "QmV1b8fa914f2e081875baeb92bf7ddd9ad5692ec2ae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289257,
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
      "evaluated_at": 1760289257
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
  "sig": "0e0717da4ede47e399644626f7a720e6e157a6fe9372779cb1b00f6098779cd6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248879476
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 22449382, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285763, 'matching_hash': '88da1f364f410d45'}}}
```json
{
  "id": "b9f9cfdc6708f1e3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290366,
  "host_pid": "9e6742732c60:1",
  "hash": "283e928c0c7d29c3c1bf7c017e19d19b21a9017652a070ead9d7341cb9b889b5",
  "cid": "QmV1283e928c0c7d29c3c1bf7c017e19d19b21a90176",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290366,
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
      "evaluated_at": 1760290366
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
  "sig": "b4e1c1e1c09858cc715f84fcbed8c19db990b7297442152195098d112a977515"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150658717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 49495344, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285765, 'matching_hash': 'c0bd022b5af03ee8'}}}
```json
{
  "id": "a75c039de9e86635",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289978,
  "host_pid": "9e6742732c60:1",
  "hash": "e99cd18b1cc2dcf7083aecd695b89697414b49371c87be37f232cb84ea7e450b",
  "cid": "QmV1e99cd18b1cc2dcf7083aecd695b89697414b4937",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289978,
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
      "evaluated_at": 1760289978
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
  "sig": "b920f327c325e9b14c3c5b2da92d8abb590834d23a05d2588be7a6b1a2227bb1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461002751
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 46386768, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285763, 'matching_hash': 'a9820f16c3d139ec'}}}
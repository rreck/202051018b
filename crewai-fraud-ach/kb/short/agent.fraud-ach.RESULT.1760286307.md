```json
{
  "id": "e0ca3fb5bd0c4bf7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286307,
  "host_pid": "9e6742732c60:1",
  "hash": "c7d1ebc7a80802eed6cc53523cc04321834ac6af9f244a81bcb6f5044886dbac",
  "cid": "QmV1c7d1ebc7a80802eed6cc53523cc04321834ac6af",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286307,
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
      "evaluated_at": 1760286307
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
  "sig": "8eb254793049397a259a77aa7e5b79ddad603f56e783472afb3a18f5e4cc6cc9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465836827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 20305980, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760284979, 'matching_hash': '8a0ab7f0e4aa4922'}}}
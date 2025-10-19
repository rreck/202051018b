```json
{
  "id": "6612e402acd6dc01",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292431,
  "host_pid": "9e6742732c60:1",
  "hash": "a6e93b7e73b1f7ba02f63744340be08968be04a69d880d1c6a68e643f5e6ed70",
  "cid": "QmV1a6e93b7e73b1f7ba02f63744340be08968be04a6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292431,
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
      "evaluated_at": 1760292431
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
  "sig": "f9505d73e27b84cfd744acb476947721638561bd7fc4449e21c36d4202a9c7fa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039498282
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 98153674, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285765, 'matching_hash': 'dad018b424b66512'}}}
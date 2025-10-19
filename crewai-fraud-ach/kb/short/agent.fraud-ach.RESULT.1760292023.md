```json
{
  "id": "8cbdc3827a84c512",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292023,
  "host_pid": "9e6742732c60:1",
  "hash": "e3476dd64281c97ba1b4480b0c4ed3de5715ffbb6f6bf2e960be661caac4e17c",
  "cid": "QmV1e3476dd64281c97ba1b4480b0c4ed3de5715ffbb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292023,
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
      "evaluated_at": 1760292023
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
  "sig": "1c1278927cabbd90659e3f6a7c625e067e7ba6a61e89b3c96176362b8fc1666d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038917834
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 54612496, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285765, 'matching_hash': '760f57350f86dbe3'}}}
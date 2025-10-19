```json
{
  "id": "51ce97f67ee1b339",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289932,
  "host_pid": "9e6742732c60:1",
  "hash": "7bf561e183956d0e91b4fb427e626edc76e8493aa8054641e9ad6835b1a594c8",
  "cid": "QmV17bf561e183956d0e91b4fb427e626edc76e8493a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289932,
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
      "evaluated_at": 1760289932
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "d092ba0ef3bf4f14a8755dc377486b88738ffbaa78570298e47cbce1130f2cb4"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 646437634699290
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 61369424, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285763, 'matching_hash': 'd218c468aa26fc36'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '646437635', 'validation_error': 'Invalid routing number checksum'}}}
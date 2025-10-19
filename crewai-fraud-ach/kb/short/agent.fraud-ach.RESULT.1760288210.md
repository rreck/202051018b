```json
{
  "id": "a3953e8993c56400",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288210,
  "host_pid": "9e6742732c60:1",
  "hash": "d194c61d767c77db0674039eb8cb9773fd5ea8f6f907293e84bae6f2a8f7a95f",
  "cid": "QmV1d194c61d767c77db0674039eb8cb9773fd5ea8f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288210,
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
      "evaluated_at": 1760288210
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
  "sig": "17c7bfacd931f5dadee9de4edbb0860d74347b037660592b34caebb54edf6aa0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270009801
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50, 'total_amount': 41615658, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285763, 'matching_hash': '0a6cdd943232be17'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '818309298', 'validation_error': 'Invalid routing number checksum'}}}
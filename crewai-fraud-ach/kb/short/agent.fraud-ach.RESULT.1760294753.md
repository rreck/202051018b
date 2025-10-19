```json
{
  "id": "1f02561986f2828d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294753,
  "host_pid": "9e6742732c60:1",
  "hash": "249c141ab9ab71b3a01a8aa7b6826006dfe3a289772d7ed5d53ebcac048a4040",
  "cid": "QmV1249c141ab9ab71b3a01a8aa7b6826006dfe3a289",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294753,
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
      "evaluated_at": 1760294753
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
  "sig": "6d04c4f50ae41859157ffa7666c039e2fd4d114ef0babd653176c8937935984c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463831807
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 43987100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': 'ac2384e4a351cc1b'}}} {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '085520764', 'validation_error': 'Invalid routing number checksum'}}}
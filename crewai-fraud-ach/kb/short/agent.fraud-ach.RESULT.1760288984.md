```json
{
  "id": "d4814cdd4d433388",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288984,
  "host_pid": "9e6742732c60:1",
  "hash": "896a13ce18f8f529cb7d40be40639d9019ca1fda5d56f7a91a4f33c9721333db",
  "cid": "QmV1896a13ce18f8f529cb7d40be40639d9019ca1fda",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288984,
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
      "evaluated_at": 1760288984
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
  "sig": "0f5a6dee8196a250cd419ede0c75e3ab2b2f93a6789a6bf639cdc5a2c4aec212"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024174154
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 46828650, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285763, 'matching_hash': '443a0c3eda74d322'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '824845890', 'validation_error': 'Invalid routing number checksum'}}}
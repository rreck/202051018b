```json
{
  "id": "0fe06d63ad35cd51",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287848,
  "host_pid": "9e6742732c60:1",
  "hash": "099a6be2f12a9ce92f9f7d054bd6d230c64d1bd902f4553dbeafe772db3323ea",
  "cid": "QmV1099a6be2f12a9ce92f9f7d054bd6d230c64d1bd9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287848,
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
      "evaluated_at": 1760287848
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
  "sig": "df8b537edc805e4d024f54674ac72bad4cc79343156cf17f9bc6a4f71d250996"
}
```

Fraud detected: invalid_routing (score: 92)
Transaction: 735962402542057
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 32822700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285764, 'matching_hash': '8fcdc870d029f888'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '735962404', 'validation_error': 'Invalid routing number checksum'}}}
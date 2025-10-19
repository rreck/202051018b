```json
{
  "id": "e2faef519c590af6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290552,
  "host_pid": "9e6742732c60:1",
  "hash": "ba9feefd1bf811e95bc681f7fc0b2cf770dbcc7172b0d3a4576f75a8ccf0f123",
  "cid": "QmV1ba9feefd1bf811e95bc681f7fc0b2cf770dbcc71",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290552,
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
      "evaluated_at": 1760290552
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
  "sig": "61e97ab00f65ff0c320816cfb6c9fbfec3d380f0cd748bbe5d4a671f47b676e6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599017181
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 27111294, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285763, 'matching_hash': '7f94592234367703'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '870312145', 'validation_error': 'Invalid routing number checksum'}}}
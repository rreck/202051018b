```json
{
  "id": "3290161ea3a3cb4f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287572,
  "host_pid": "9e6742732c60:1",
  "hash": "dede83dadd737a3cc8849a5e53733b6ff7b85fd6342661fc89323f3a95998f43",
  "cid": "QmV1dede83dadd737a3cc8849a5e53733b6ff7b85fd6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287572,
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
      "evaluated_at": 1760287572
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
  "sig": "21807d76a9a9d5ef395b94942a97e4f1614c1e183d90b21eb5f6487d5793adab"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 026009590857246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50, 'total_amount': 23036390, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285763, 'matching_hash': 'f091f96bdb04a5bf'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '864091464', 'validation_error': 'Invalid routing number checksum'}}}
```json
{
  "id": "1b67d0a85467239a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293160,
  "host_pid": "9e6742732c60:1",
  "hash": "7ebe1220671cb50d1842182d193d31dcf76ecc60f392aeb4f7b572f273abcda6",
  "cid": "QmV17ebe1220671cb50d1842182d193d31dcf76ecc60",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293160,
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
      "evaluated_at": 1760293160
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
  "sig": "5e5c50e150484bba070dfbaf5836a523bffb4709dd7cd34c06f9b6b7979e97d0"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 561028999821965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 29817657, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': '09f745cfd1242827'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '561028991', 'validation_error': 'Invalid routing number checksum'}}}
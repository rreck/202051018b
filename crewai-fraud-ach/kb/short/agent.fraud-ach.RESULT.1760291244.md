```json
{
  "id": "b3cc1695fe9bfcaa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291244,
  "host_pid": "9e6742732c60:1",
  "hash": "885502ef0f4ff24a9b56b049a599ac247120a0c0c6fb5f87709ae6508439b510",
  "cid": "QmV1885502ef0f4ff24a9b56b049a599ac247120a0c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291244,
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
      "evaluated_at": 1760291244
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
  "sig": "9855318e8c939617cfea2be2875247dd851968293554df0ca5bfbe2562a2211b"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 683146203883533
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 63311740, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285764, 'matching_hash': '8f404d0fc37310f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '683146208', 'validation_error': 'Invalid routing number checksum'}}}
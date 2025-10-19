```json
{
  "id": "ee1e153567033d29",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294407,
  "host_pid": "9e6742732c60:1",
  "hash": "1d6a900e4a13689c5a90be530655d4c63fb11cb0c724df7532e9301ff3ae93b3",
  "cid": "QmV11d6a900e4a13689c5a90be530655d4c63fb11cb0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294407,
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
      "evaluated_at": 1760294407
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
  "sig": "3bcf2800b35b01f818918f18cef65b43ed5df0258948f9a5d2a4d78483321272"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242634243
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 106199463, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285764, 'matching_hash': '8925ee68733f12e3'}}}
```json
{
  "id": "dc6e0e2190c0d9ec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293425,
  "host_pid": "9e6742732c60:1",
  "hash": "fcfed00ac55dfde39ff7d3609c5f4f23628893d2340ee3fb44e1c8fa0aebd5b4",
  "cid": "QmV1fcfed00ac55dfde39ff7d3609c5f4f23628893d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293425,
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
      "evaluated_at": 1760293425
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
  "sig": "eadd289dc421651dd61382b5b199cb8d439fb61de17fd046d458d016e5ccee1a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026466423
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 102945268, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285764, 'matching_hash': '1fcdc28f16166b10'}}}
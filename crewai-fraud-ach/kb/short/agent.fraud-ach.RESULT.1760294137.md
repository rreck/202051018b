```json
{
  "id": "bcfd32d3fadef8eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294137,
  "host_pid": "9e6742732c60:1",
  "hash": "5c60ced2ff30e826a9e375bc2cde09cd3963f9cae333a29c69c3d5e6a7ee03d6",
  "cid": "QmV15c60ced2ff30e826a9e375bc2cde09cd3963f9ca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294137,
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
      "evaluated_at": 1760294138
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
  "sig": "121df7fba28262fab5d6908e56ea11e79004d788cf257a8e61950ed3972da9be"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594239738
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 308, 'threshold': 50, 'total_amount': 65553488, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 307, 'first_seen': 1760284979, 'matching_hash': '98c544a6e0691c0b'}}}
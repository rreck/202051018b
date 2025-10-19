```json
{
  "id": "ad46f373ed1014a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290150,
  "host_pid": "9e6742732c60:1",
  "hash": "28472705a11830dbca409551dae45cf5ce51f3cdacbaedc1aafa23f70fe5c599",
  "cid": "QmV128472705a11830dbca409551dae45cf5ce51f3cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290150,
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
      "evaluated_at": 1760290150
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
  "sig": "a9e0a41a7ba01ffa613ad8551b18c2c927ed36767c2d4bec50992906e3453a05"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594497049
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 29290833, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285763, 'matching_hash': 'c5255ffe70702a12'}}}
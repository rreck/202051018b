```json
{
  "id": "24930b728368887e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292838,
  "host_pid": "9e6742732c60:1",
  "hash": "4d4cc0e2f8017513866da089a929f2bce6692933345aaf974b17f4bf6edd2502",
  "cid": "QmV14d4cc0e2f8017513866da089a929f2bce6692933",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292838,
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
      "evaluated_at": 1760292838
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
  "sig": "83688f40782b126a7ce1bd7f8bf7408fba328ba66919da4b0f9498f4235d41a8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156493582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 26478004, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': '28d5522bb9de7370'}}}
```json
{
  "id": "4382121ce452e2d3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290345,
  "host_pid": "9e6742732c60:1",
  "hash": "2d0a52c28fddd7541a3bcdbe18d0f7cc37eb0013f83ed8285dc967bcb92a1224",
  "cid": "QmV12d0a52c28fddd7541a3bcdbe18d0f7cc37eb0013",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290345,
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
      "evaluated_at": 1760290345
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
  "sig": "639d5b4c46332ef849fdcc0eb03689c3c979b62e1d49bec9697239100a61fa14"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249225817
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 34861252, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285763, 'matching_hash': 'b4dc0a1cb279f16e'}}}
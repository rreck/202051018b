```json
{
  "id": "aeeeec7e92a0d8aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290500,
  "host_pid": "9e6742732c60:1",
  "hash": "e93f28b152e610a031945e23466cc352920b9287c21c1c06a32cc904ec29dcf3",
  "cid": "QmV1e93f28b152e610a031945e23466cc352920b9287",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290500,
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
      "evaluated_at": 1760290500
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
  "sig": "2a5fb455b2c2883a683a0a211c6b8790d8b3f6f38ec291670a091339d8394a9c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240814513
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 44999296, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285763, 'matching_hash': '8ef20234ae18fb17'}}}
```json
{
  "id": "0ca932901c79ccfc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294322,
  "host_pid": "9e6742732c60:1",
  "hash": "6aa23c10b3321c898ccc4f59e94901d9a4a76d3fcbcf66f9bea26942715e7bd3",
  "cid": "QmV16aa23c10b3321c898ccc4f59e94901d9a4a76d3f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294322,
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
      "evaluated_at": 1760294322
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
  "sig": "9d3cf59506920f4d373d8c58d3fd0976d527e3381a5757f084d1a931950cca2d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025810032
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 115583124, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': '4a1b4df87be22a11'}}}
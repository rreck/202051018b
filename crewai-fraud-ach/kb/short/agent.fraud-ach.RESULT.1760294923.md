```json
{
  "id": "08c21d89a10e4624",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294923,
  "host_pid": "9e6742732c60:1",
  "hash": "5a12490d8ba259aa7915b9636b2dc3ad02e70fa25c78723dc988a95ab010da24",
  "cid": "QmV15a12490d8ba259aa7915b9636b2dc3ad02e70fa2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294923,
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
      "evaluated_at": 1760294923
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
  "sig": "b106345026ea340463101cdd50e556798104dbfc8fb0eb99838bbc65f8c37af2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240814513
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 247, 'threshold': 50, 'total_amount': 73123856, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 246, 'first_seen': 1760285763, 'matching_hash': '8ef20234ae18fb17'}}}
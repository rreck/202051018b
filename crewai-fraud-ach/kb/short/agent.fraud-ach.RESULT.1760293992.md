```json
{
  "id": "8363567d2db4e0ce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293992,
  "host_pid": "9e6742732c60:1",
  "hash": "26068f8a568b6268ae111489b19a7fd0b2a0ff2d03f43f6f6a2c9cea7d6d1f1d",
  "cid": "QmV126068f8a568b6268ae111489b19a7fd0b2a0ff2d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293992,
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
      "evaluated_at": 1760293992
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
  "sig": "7d1d43bc7920ff68056eaa62e47359e72f086addf0197fd1f64d2350f4e7c160"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034020503
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 11450000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285765, 'matching_hash': '8db66b2beb557931'}}}
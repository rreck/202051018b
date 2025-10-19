```json
{
  "id": "aa2f6c377bd8ecfa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286562,
  "host_pid": "9e6742732c60:1",
  "hash": "2cd45d4d78c5cfd613341d35221b3a31003736cbf2a0e914963a3b78fef84d07",
  "cid": "QmV12cd45d4d78c5cfd613341d35221b3a31003736cb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286562,
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
      "evaluated_at": 1760286562
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "ba304e19ddcbc4541dec090230a46e7880c86041b443eb63bf89ba629ad158f0"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 845955323982908
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10467666, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285765, 'matching_hash': '603efe89834eadf7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '845955329', 'validation_error': 'Invalid routing number checksum'}}}
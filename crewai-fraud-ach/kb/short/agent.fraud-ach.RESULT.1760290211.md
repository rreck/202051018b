```json
{
  "id": "45bf600155104eab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290211,
  "host_pid": "9e6742732c60:1",
  "hash": "701ee619d068f88f85cea698968e86c790391229a7207c4b7fbd722af13a98e4",
  "cid": "QmV1701ee619d068f88f85cea698968e86c790391229",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290211,
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
      "evaluated_at": 1760290211
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
  "sig": "38017fe216b6ae572c08701a533ae3414c2ad813c8418a3c5a09ef040c70537d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029278927
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 41612256, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285765, 'matching_hash': '45338af8ff50831c'}}}
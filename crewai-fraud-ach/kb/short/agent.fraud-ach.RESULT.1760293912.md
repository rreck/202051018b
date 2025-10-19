```json
{
  "id": "5bcef3f266cd4fb5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293912,
  "host_pid": "9e6742732c60:1",
  "hash": "60fc61e6ef4e01547ede5aee5ba0606f4bd6d872d5e47e717cd471a78dc13e30",
  "cid": "QmV160fc61e6ef4e01547ede5aee5ba0606f4bd6d872",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293912,
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
      "evaluated_at": 1760293912
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
  "sig": "addaa771426fecfdf8e7956d6f38e66fa0c0480871210b83893898be611e27fa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027679172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 99010824, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': 'bcf2a51730a73925'}}}
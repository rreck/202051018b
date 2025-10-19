```json
{
  "id": "8721b80a222fb4b0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294335,
  "host_pid": "9e6742732c60:1",
  "hash": "43e31547cdac2618e578fec0ba81807e45ff259e07a0fe1ac7e514e97da768ec",
  "cid": "QmV143e31547cdac2618e578fec0ba81807e45ff259e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294335,
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
      "evaluated_at": 1760294335
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
  "sig": "4e53cacb9960dfc90db6a2798f2c4acdb024908aebd1f7635b2f5ecf498fc0d8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468482875
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 29742372, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285764, 'matching_hash': '502f46d9d0122688'}}}
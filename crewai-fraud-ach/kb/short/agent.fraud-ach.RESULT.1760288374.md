```json
{
  "id": "0b136235e268e6cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288374,
  "host_pid": "9e6742732c60:1",
  "hash": "472f33264a6cc1cd444c6453561b8b84537e0275de1372d677a6daa7e368514b",
  "cid": "QmV1472f33264a6cc1cd444c6453561b8b84537e0275",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288374,
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
      "evaluated_at": 1760288374
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
  "sig": "bead68d6feca4e23d0086b37fb64ba1f544cd74d0d1812afdf35f247f3a95c20"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240022849
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 30344132, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285765, 'matching_hash': 'fbe681be7d902297'}}}
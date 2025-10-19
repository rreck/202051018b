```json
{
  "id": "a68605d34a0a49e2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294610,
  "host_pid": "9e6742732c60:1",
  "hash": "c25d8d72b4f21c7c19023a80149076eda511561761d4e62843843fd2015fcb0a",
  "cid": "QmV1c25d8d72b4f21c7c19023a80149076eda5115617",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294610,
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
      "evaluated_at": 1760294610
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
  "sig": "fe79adba76a3d0cc21267834896586fffc2b4360c535e2a283e0a78eedd08d4f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029347324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 37104119, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': '03de14fe5a3852ae'}}}}
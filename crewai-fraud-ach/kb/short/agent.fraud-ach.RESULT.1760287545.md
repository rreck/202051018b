```json
{
  "id": "b46944c6f3d2e388",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287545,
  "host_pid": "9e6742732c60:1",
  "hash": "bcbf5392b009006be5afeae8e2af582601eb1b9f6fe596118ab835da4b1cc944",
  "cid": "QmV1bcbf5392b009006be5afeae8e2af582601eb1b9f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287545,
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
      "evaluated_at": 1760287545
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
  "sig": "397a37d76f02f6fd45892072e6c877b3e3756b964f55a6430f40a455854089bc"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 122105150980279
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50, 'total_amount': 14389760, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285763, 'matching_hash': '8a0222b527408f48'}}}
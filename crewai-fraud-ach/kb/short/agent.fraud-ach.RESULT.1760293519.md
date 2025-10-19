```json
{
  "id": "d9a29831d6e7434e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293519,
  "host_pid": "9e6742732c60:1",
  "hash": "543f148c5125cfb9e83256aee8774c592fdedf0629bd05270b15eda242593936",
  "cid": "QmV1543f148c5125cfb9e83256aee8774c592fdedf06",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293519,
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
      "evaluated_at": 1760293519
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
  "sig": "4e24d7de44637d01e1bb11eba4bcc2883b7c8912ade2bd0eb6d220697eb879f2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465310802
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 82283740, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': '86dc5261411570c1'}}}